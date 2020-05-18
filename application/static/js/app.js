document.querySelector('.theme-toggle-button').addEventListener('click', () => {
  document.body.classList.toggle('light');
});

const surveys_url = `${api_base_url}/surveys`;
const table = d3.select('#survey-responses-table');
const tableBody = table.select('tbody');
const tableHeaderRow = table.select('.table-header-row')

d3.json(surveys_url).then(data => {
  data.result.forEach(item => {
    let newRow = tableBody.append('tr');

    Object.entries(item).forEach(function ([key, value]) {
      if (key !== 'id') {
        newRow.append('td').text(value != null ? value.toString() : '');
      }
    });
  });
});

const sentiment_scores_url = `${api_base_url}/sentiment_scores`;
const sentimentScoresTable = d3.select('#sentiment-scores-table');
const sentimentScoresTableBody = sentimentScoresTable.select('tbody');
const sentimentScoresTableHeaderRow = sentimentScoresTable.select('.table-header-row')

d3.json(sentiment_scores_url).then(data => {
  console.log(data)
  data.result.forEach(item => {
    let newRow = sentimentScoresTableBody.append('tr');

    Object.entries(item).forEach(function ([key, value]) {
      if (key !== 'id') {
        newRow.append('td').text(value);
      }
    });
  });
});
