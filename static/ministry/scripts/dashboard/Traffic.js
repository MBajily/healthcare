zingchart.MODULESDIR = 'https://cdn.zingchart.com/modules/';

zingchart.defineModule('toolbar-zoom', 'plugin', function (chartJson) {
  /*
   * If the 'labels' array of objects already exists, do nothing.
   * If it does not exist, initialize it as an empty array.
   * We do this to avoid obliteration of any existing labels.
   */
  chartJson.labels = chartJson.labels ? chartJson.labels : [];

  /* Push the toolbar label objects */
  chartJson.labels.push(
    {
      type: 'rectangle',
      id: 'zoomin',
      width: '30px',
      height: '30px',
      backgroundColor: 'none',
      backgroundImage:
        'https://cdn4.iconfinder.com/data/icons/miu/22/editor_zoom-in_-20.png',
      backgroundRepeat: 'no-repeat',
      cursor: 'hand',
      marginTop: '10px',
      marginLeft: '50px',
      marginRight: 'auto',
      borderWidth: '1px',
      borderColor: '#aaa',
      borderRadiusTopLeft: '5px',
      borderRadiusBottomLeft: '5px',
      zIndex: 1,
    },
    {
      type: 'rectangle',
      id: 'zoomout',
      width: '30px',
      height: '30px',
      backgroundColor: 'none',
      backgroundImage:
        'https://cdn4.iconfinder.com/data/icons/miu/22/editor_zoom-out_-20.png',
      backgroundRepeat: 'no-repeat',
      cursor: 'hand',
      marginTop: '10px',
      marginLeft: '80px',
      marginRight: 'auto',
      borderWidth: '1px',
      borderColor: '#aaa',
      zIndex: 1,
    },
    {
      type: 'rectangle',
      id: 'viewall',
      width: '30px',
      height: '30px',
      backgroundColor: 'none',
      backgroundImage:
        'https://cdn1.iconfinder.com/data/icons/freeline/32/eye_preview_see_seen_view-20.png',
      backgroundRepeat: 'no-repeat',
      cursor: 'hand',
      marginTop: '10px',
      marginLeft: '110px',
      marginRight: 'auto',
      borderWidth: '1px',
      borderColor: '#aaa',
      borderRadiusTopRight: '5px',
      borderRadiusBottomRight: '5px',
      zIndex: 1,
    }
  );

  /*
   * Add label_click event listener, use the clicked label's
   * id in a switch
   */
  zingchart.label_click = function (p) {
    switch (p.labelid) {
      case 'zoomin':
        zingchart.exec(p.id, 'zoomin');
        break;
      case 'zoomout':
        zingchart.exec(p.id, 'zoomout');
        break;
      case 'viewall':
        zingchart.exec(p.id, 'viewall');
        break;
    }
  };

  /* Create a reference to the "toolbar-zoom" object */
  let optionsObj = chartJson['toolbar-zoom'];
  /*
   * If the "background-color" attr exists, loop over each label and
   * modify the background-color on those with certain "id" values.
   */
  if (optionsObj['background-color']) {
    for (let n in chartJson['labels']) {
      let labelObj = chartJson['labels'][n];
      if (
        labelObj['id'] == 'zoomin' ||
        labelObj['id'] == 'zoomout' ||
        labelObj['id'] == 'viewall'
      ) {
        labelObj['background-color'] = optionsObj['background-color'];
      }
    }
  }
  /* Same thing as above, but for border-color.  */
  if (optionsObj['border-color']) {
    for (let n in chartJson['labels']) {
      let labelObj = chartJson['labels'][n];
      if (
        labelObj['id'] == 'zoomin' ||
        labelObj['id'] == 'zoomout' ||
        labelObj['id'] == 'viewall'
      ) {
        labelObj['border-color'] = optionsObj['border-color'];
      }
    }
  }
  return chartJson;
});

// let trafficChartConfig = {
//   type: 'bar',
//   title: {
//     text: 'Traffic',
//   },
//   'toolbar-zoom': {
//     // Add the toolbar
//     'background-color': '#FFFFFF #D0D7E1',
//     'border-color': '#ACAFB6',
//   },
//   scaleX: {
//     zooming: true,
//   },
//   series: [
//     {
//       values: [35, 42, 67, 89, 25, 34, 67, 85,24,53,35,24,76,35,34,75,13,15,63,23,63,25,75,34,65,35,76,86,54,76],
//     },
//   ],
//   scrollX: {},
// };

// zingchart.render({
//   id: 'Traffic',
//   data: trafficChartConfig,
//   height: '400px',
//   width: '100%',
//   modules: 'toolbar-zoom', // Load the toolbar
// });