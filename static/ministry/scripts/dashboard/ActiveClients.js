// CHART CONFIG
// -----------------------------
let activeClientsChartConfig = {
  type: 'bar',
  backgroundColor: '#ffffff',
  title: {
    text: 'Click And Drag To Select',
  },
  subtitle: {
    text: 'Click To Clear Selection',
  },
  legend: {
    adjustLayout: false,
    align: 'center',
    borderWidth: '0px',
    fontColor: '#7d7d7d',
    fontSize: '10px',
    marginBottom: '0px',
    marginRight: '20px',
    marginTop: '0px',
    marker: {
      type: 'square',
    },
    toggleAction: 'remove',
    verticalAlign: 'bottom',
  },
  plot: {
    tooltip: {
      text: '%kl<br>%vv',
      visible: true,
    },
    backgroundColor: '#1e88e5',
    dataAppendSelection: true,
    lineColor: '#4d9900',
    lineWidth: '1px',
    marker: {
      backgroundColor: '#ccccff #6666ff',
      borderColor: '#4d9900',
      borderWidth: '1px',
      size: '3px',
    },
    mode: 'normal',
    selectedState: {
      backgroundColor: '#ffa726',
      borderWidth: '0px',
    },
    selectionMode: 'multiple',
  },
  plotarea: {
    margin: 'dynamic 50px 105px dynamic',
    marginTop: '20px',
    marginLeft: '20px',
  },
  scaleX: {
    item: {
      fontColor: '#7d7d7d',
      fontSize: '10px',
    },
    minValue: 1547802007000,
    step: 'day',
    tick: {
      visible: false,
    },
    title: {
      text: 'You can Make Multiple Selections And Click To Clear selection',
    },
    transform: {
      type: 'date',
    },
    zooming: true,
    zoomTo: [0, 30],
  },
  scaleY: {
    values: '0:2.503:0.5006',
    decimals: 1,
    format: '%v%',
    guide: {
      lineStyle: 'dotted',
    },
    item: {
      fontColor: '#7d7d7d',
      fontSize: '10px',
    },
    tick: {
      visible: false,
    },
    zooming: false,
  },
  zoom: {
    active: false,
    preserveZoom: true,
  },
  preview: {
    backgroundColor: '#F5F7F3',
    borderWidth: '0px',
    handle: {
      borderWidth: '1px',
    },
    height: '29px',
    mask: {
      alpha: 0.8,
      backgroundColor: 'white',
    },
    preserveZoom: false,
    y: '85%',
  },
  series: [
    {
      text: 'Percentage Of Sales',
      values: [
        0.8840000000000001, 1.9060000000000001, 1.35, 1.189, 0.984, 0.619,
        0.468, 0.28700000000000003, 2.503, 1.139, 2.011, 1.7389999999999999,
        0.5559999999999999, 0.22899999999999998, 0.218, 0.761, 0.58, 1.171,
        0.8240000000000001, 0.721, 0.542, 0.954, 0.683, 0.976,
        1.0290000000000001, 0.28800000000000003, 0.362, 0.388, 1.057, 0.886,
        0.196, 0.333, 1.013, 0.541, 0.127, 0.726, 0.649, 1.031, 0.606, 1.232,
        0.5459999999999999, 0.8340000000000001, 1.9869999999999999, 0.257, 0.62,
        0.571, 0.194, 0.315, 0.45799999999999996, 0.14300000000000002, 0.126,
        0.252, 0.588, 1.419, 0.259, 0.724, 0.295, 0.344, 0.455,
        0.27699999999999997, 0.604, 0.471, 0.8200000000000001, 0.504, 0.209,
        0.33999999999999997, 0.404, 0.127, 0.293, 0.326, 0.428,
        0.38999999999999996, 0.562, 0.14300000000000002, 0.258, 0.414,
        0.42100000000000004, 0.6669999999999999, 0.8290000000000001, 1.369,
        0.261, 1.15, 0.644, 0.519, 0.44400000000000006, 0.627, 0.411, 0.447,
        0.173, 0.763, 0.581, 1.2710000000000001, 0.9129999999999999, 0.988,
        0.51, 0.664, 0.348, 0.5559999999999999, 0.28600000000000003, 0.424,
        0.676, 0.367, 0.634, 0.47600000000000003, 0.512, 0.33999999999999997,
        0.076, 0.27799999999999997, 0.291, 0.402, 0.199, 0.21, 0.261, 0.178,
        0.315, 0.6459999999999999, 0.482, 0.08499999999999999, 0.068,
        0.40099999999999997, 0.135, 0.679, 0.769, 1.113, 0.315, 0.37, 0.267,
        0.145, 1.2309999999999999, 0.126, 0.217, 1.0670000000000002, 2.213,
        0.687, 0.63, 0.498, 0.428, 0.154, 0.27299999999999996, 0.161,
        0.28900000000000003, 0.8130000000000001, 0.406, 0.553, 0.584, 0.73,
        0.347, 0.194, 0.439, 0.28800000000000003, 0.561, 0.22499999999999998,
        1.2550000000000001, 0.771, 0.13, 0.644, 0.078, 0.27899999999999997,
        0.35100000000000003, 0.525, 0.735, 0.893, 0.719, 1.375,
        0.42500000000000004, 0.27999999999999997, 0.255, 0.109, 0.411, 0.11,
        0.172, 0.698,
      ],
    },
  ],
};

// EVENTS
// -----------------------------
zingchart.bind('ActiveClients', 'click', (e) => {
  if (e.target === 'none') {
    zingchart.exec('ActiveClients', 'clearselection');
  }
});

// RENDER CHARTS
// -----------------------------
// Load the selection-tool and render the chart once its loaded
zingchart.loadModules('selection-tool', () => {
  zingchart.render({
    id: 'ActiveClients',
    data: activeClientsChartConfig,
    modules: 'selection-tool',
  });
});