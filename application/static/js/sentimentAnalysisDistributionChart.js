// Define SVG area dimensions
const svgWidth = 960;
const svgHeight = 660;

// Define the chart's margins as an object
const chartMargin = {
  top: 30,
  right: 30,
  bottom: 30,
  left: 30
};

// Define dimensions of the chart area
const chartWidth = svgWidth - chartMargin.left - chartMargin.right;
const chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

// Select body, append SVG area to it, and set the dimensions
const svgVader = d3.select("#vader-results-chart")
  .append("svg")
  .attr("viewBox", `0 0 ${svgWidth} ${svgHeight}`)

const svgTextblob = d3.select("#textblob-results-chart")
  .append("svg")
  .attr("viewBox", `0 0 ${svgWidth} ${svgHeight}`)

// Append a group to the SVG area and shift ('translate') it to the right and to the bottom
const chartGroupVader = svgVader.append("g")
  .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);

const chartGroupTextblob = svgTextblob.append("g")
  .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);

const sentiment_results_url = `${api_base_url}/sentiment_scores`;
// Load data from hours-of-tv-watched.csv
d3.json(sentiment_results_url).then(function (data) {

  const dataCategories = ["positive", "neutral", "negative"];
  const vaderResults = [data.number_positive_vader, data.number_neutral_vader, data.number_negative_vader];
  const textblobResults = [data.number_positive_textblob, data.number_neutral_textblob, data.number_negative_textblob];

  // scale y to chart height
  const yScaleVader = d3.scaleLinear()
    .domain([0, d3.max(vaderResults)])
    .range([chartHeight, 0]);

  const yScaleTextblob = d3.scaleLinear()
    .domain([0, d3.max(vaderResults)])
    .range([chartHeight, 0]);

  // scale x to chart width
  const xScaleVader = d3.scaleBand()
    .domain(dataCategories)
    .range([0, chartWidth])
    .padding(0.05);

  const xScaleTextblob = d3.scaleBand()
    .domain(dataCategories)
    .range([0, chartWidth])
    .padding(0.05);

  // create axes
  const yAxisVader = d3.axisLeft(yScaleVader);
  const xAxisVader = d3.axisBottom(xScaleVader);

  const yAxisTextblob = d3.axisLeft(yScaleTextblob);
  const xAxisTextblob = d3.axisBottom(xScaleTextblob);

  // set x to the bottom of the chart
  chartGroupVader.append("g")
    .attr("transform", `translate(0, ${chartHeight})`)
    .style("font", "24px times")
    .call(xAxisVader);

  chartGroupTextblob.append("g")
    .attr("transform", `translate(0, ${chartHeight})`)
    .style("font", "24px times")
    .call(xAxisVader);

  // set y to the y axis
  // This syntax allows us to call the axis function
  // and pass in the selector without breaking the chaining
  chartGroupVader.append("g")
    .style("font", "20px times")
    .call(yAxisVader);

  chartGroupTextblob.append("g")
    .style("font", "20px times")
    .call(yAxisTextblob);

  // Append Data to chartGroup
  chartGroupVader.selectAll(".bar")
    .data(vaderResults)
    .enter()
    .append("rect")
    .classed("bar", true)
    .attr("x", (d, i) => xScaleVader(dataCategories[i]))
    .attr("y", d => yScaleVader(d))
    .attr("width", xScaleVader.bandwidth())
    .attr("height", d => chartHeight - yScaleVader(d))
    .attr("fill", 'lightpink');

  // Append Data to chartGroup
  chartGroupTextblob.selectAll(".bar")
    .data(textblobResults)
    .enter()
    .append("rect")
    .classed("bar", true)
    .attr("x", (d, i) => xScaleTextblob(dataCategories[i]))
    .attr("y", d => yScaleTextblob(d))
    .attr("width", xScaleTextblob.bandwidth())
    .attr("height", d => chartHeight - yScaleTextblob(d))
    .attr("fill", 'lightpink');

}).catch(function (error) {
  console.log(error);
});
