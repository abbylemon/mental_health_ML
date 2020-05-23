// Define SVG area dimensions
const svgWidthPredict = 960;
const svgHeightPredict = 660;

// Define the chart's margins as an object
const chartMarginPredict = {
  top: 30,
  right: 50,
  bottom: 80,
  left: 50
}; 

// Define dimensions of the chart area
const chartWidthPredict = svgWidthPredict - chartMarginPredict.left - chartMarginPredict.right;
const chartHeightPredict = svgHeightPredict - chartMarginPredict.top - chartMarginPredict.bottom;

// Select body, append SVG area to it, and set the dimensions
const svgPredict = d3.select("#twenty20-predict-chart")
  .append("svg")
  .attr("viewBox", `0 0 ${svgWidthPredict} ${svgHeightPredict}`);

// Append a group to the SVG area and shift ('translate') it to the right and to the bottom
const chartGroup = svgPredict.append("g")
  .attr("transform", `translate(${chartMarginPredict.left}, ${chartMarginPredict.top})`);


d3.csv("/static/predictChartData.csv")
    .then(function (predictData) {
        
      predictData.forEach(function (data) {
        data.TruePrecent = +data.TruePrecent;
        data.FalsePercent = +data.FalsePercent;
        console.log(data.Year);
      });
      console.log(predictData);

      // scale y to chart height
      const yScale = d3.scaleLinear()
      .domain([0, d3.max(predictData, d => d.TruePrecent)+0.1])
      .range([chartHeightPredict, 0]);

      // scale x to chart width
      const xScale = d3.scaleBand()
      // .domain([0, d3.range(predictData, d => d.Year)])
      // domain(data.map(d => d.name)
      .domain(predictData.map(d => d.Year))
      // .domain([0, (predictData, d3.range(d => d.Year))])
      .range([0, chartWidthPredict])
      .padding(0.05);

      // create axes
      const yAxis = d3.axisLeft(yScale);
      const xAxis = d3.axisBottom(xScale);

      // set x to the bottom of the chart
      chartGroup.append("g")
        .attr("transform", `translate(0, ${chartHeightPredict})`)
        .call(xAxis);

      // set y to the y axis
      // This syntax allows us to call the axis function
      // and pass in the selector without breaking the chaining
      chartGroup.append("g")
        .call(yAxis);

      // Append Data to chartGroup
      var rectGroup = chartGroup.selectAll("rect")
        .data(predictData)
        .enter()
        .append("rect")
        .classed("bar", true)
        .attr("x", d => xScale(d.Year))
        .attr("y", d => yScale(d.TruePrecent))
        .attr("width", xScale.bandwidth())
        .attr("height", d => chartHeightPredict - yScale(d.TruePrecent));

      // append y axis
      chartGroup.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - chartMarginPredict.left)
        .attr("x", 0 - (svgHeightPredict / 2))
        .attr("dy", "1em")
        .style("fill", "white")
        .classed("axis-text", true)
        .text("True Responses (%)");

      // append x axis
      chartGroup.append("text")
        .attr("transform", `translate(${chartWidthPredict / 2}, ${chartHeightPredict + 30})`)
        .attr("y", 0)
        .attr("x", 20)
        .style("fill", "white")
        .classed("axis-text", true)
        .text("Year");

      // Step 1: Append tooltip div
      var toolTip = d3.select("#twenty20-predict-chart")
        .append("div")
        .classed("tooltip", true);

      // Step 2: Create "mouseover" event listener to display tooltip
      rectGroup.on("mouseover", function(d) {
        toolTip.style("display", "block")
            .html(
              `<strong>${d.Year}<strong><hr>${d.TruePrecent}`)
            .style("position", "absolute")
            .style("width", "80px")
            .style("height", "50px")
            .style("padding", "10px")
            .style("text-align", "center")
            .style("color", "white")
            .style("background", "grey")
            .style("left", d3.event.pageX + "px")
            .style("top", d3.event.pageY + "px");
      })
        // Step 3: Create "mouseout" event listener to hide tooltip
        .on("mouseout", function() {
          toolTip.style("display", "none");
        });

    }).catch(function (error) {
      console.log(error);
  });




