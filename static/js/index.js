$(function() {

"use strict";		
	
// chart2
var ctx = document.getElementById('chart2-1').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'pie',
  data: {
      labels: ['Writers', 'Developers'],
      datasets: [{
          data: [856, 2602],
          backgroundColor: [
		      "#ffffff",
			  "rgba(255, 255, 255, 0.25)"
          ],
          borderWidth: [0, 0]
      }]
  },
  options: {
      maintainAspectRatio: false,
      cutout: 100,
      plugins: {
      legend: {
          display: false,
      }
  }      
  }
});

var ctx = document.getElementById('chart2-2').getContext('2d');
var myChart = new Chart(ctx, {
	type: 'pie',
	data: {
		labels: ['Writers', 'Developers'],
		datasets: [{
			data: [856, 2602],
			backgroundColor: [
				"#ffffff",
				"rgba(255, 255, 255, 0.25)"
			],
			borderWidth: [0, 0]
		}]
	},
	options: {
		maintainAspectRatio: false,
		cutout: 100,
		plugins: {
		legend: {
			display: false,
		}
	}      
	}
  });

var ctx = document.getElementById('chart2-3').getContext('2d');
var myChart = new Chart(ctx, {
	type: 'pie',
	data: {
		labels: ['Writers', 'Developers'],
		datasets: [{
			data: [856, 2602],
			backgroundColor: [
				"#ffffff",
				"rgba(255, 255, 255, 0.25)"
			],
			borderWidth: [0, 0]
		}]
	},
	options: {
		maintainAspectRatio: false,
		cutout: 100,
		plugins: {
		legend: {
			display: false,
		}
	}      
	}
  });

  var ctx = document.getElementById('chart2-4').getContext('2d');
  var myChart = new Chart(ctx, {
	  type: 'pie',
	  data: {
		  labels: ['Present', 'Absent'],
		  datasets: [{
			  data: [856, 2602],
			  backgroundColor: [
				  "#ffffff",
				  "rgba(255, 255, 255, 0.25)"
			  ],
			  borderWidth: [0, 0]
		  }]
	  },
	  options: {
		  maintainAspectRatio: false,
		  cutout: 100,
		  plugins: {
		  legend: {
			  display: false,
		  }
	  }      
	  }
	});
});