
// full ZingChart schema can be found here:
// https://www.zingchart.com/docs/api/json-configuration/
// let bluePalette = ['#afecfe', '#7ddefd', '#36b6f8', '#3290be', '#5ca5ca', '#a0bed6', '#98c1de', '#aedaf2'];
// let chartData = [
//   {
//     values: [12.5],
//     text: 'One'
//   },
//   {
//     values: [12.5],
//     text: 'Two'
//   },
//   {
//     values: [12.5],
//     text: 'Three'
//   },
//   {
//     values: [12.5],
//     text: 'Four'
//   },
//   {
//     values: [12.5],
//     text: 'Five'
//   },
//   {
//     values: [12.5],
//     text: 'Six'
//   },
//   {
//     values: [12.5],
//     text: 'Seven'
//   },
//   {
//     values: [12.5],
//     text: 'Eight'
//   }
];

// let nationalitiesChartConfig = {
//   type: 'pie',
//   title: {
//     text: 'Nationalities',
//     color: '#5D7D9A',
//     align: 'left',
//     padding: '30 0 0 35',
//     fontSize: '30px'
//   },
//   subtitle: {
//     text: '<br>Unleash the power of the ZingChart\'s<br>advanced pie chart options to create<br>animated and interactive pie charts<br>with wildly different styles!',
//     color: '#5D7D9A',
//     fontSize: '16px',
//     fontWeight: 300,
//     align: 'left',
//     padding: '35 0 0 35'
//   },
//   shapes: {
//     type: 'triangle'
//   },
//   globals: {
//     fontFamily: 'sans-serif'
//   },
//   palette: bluePalette,
//   legend: {
//     layout: '2x4',
//     highlightPlot: true,
//     item: {
//       fontColor: '#373a3c',
//       fontSize: '12px'
//     },
//     toggleAction: 'remove',
//     align: 'left',
//     verticalAlign: 'middle',
//     margin: '5px 20px 0 25px',
//     padding: '5px',
//     borderRadius: '5px',
//     header: {
//       text: 'Legend',
//       color: '#5D7D9A',
//       padding: '10px'
//     }
//   },
//   plot: {
//     slice: '0',
//     pieTransform: 'fold=20',
//     valueBox: {
//       fontColor: '#fff'
//     },
//     detach: false,
//     highlightState: {
//       borderColor: '#000',
//       borderWidth: '2px'
//     },
//     refAngle: 270
//   },
//   labels: [

//   ],
//   tooltip: {
//     padding: '10px 15px',
//     borderRadius: '3px'
//   },
//   series: chartData
// };

// // render chart
// zingchart.render({
//   id: 'Nationalities',
//   data: nationalitiesChartConfig,
//   height: '100%',
//   width: '100%'
// });