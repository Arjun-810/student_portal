var app = angular.module('mainApp', ['gridster','ui.router', 'chart.js', 'ui.calendar']);

app.controller('mainCtrl', ['$scope', function ($scope) {
  $scope.editEnabled=true;
  $scope.templates = ["template1", "template2", "template3", "template4", "template5"]
  $scope.standardItems = [
    { sizeX: 6, sizeY: 2, row: 0, col: 0 },
    { sizeX: 4, sizeY: 3, row: 2, col: 0 },
    { sizeX: 2, sizeY: 3, row: 2, col: 4 },
    { sizeX: 3, sizeY: 3, row: 4, col: 0 },
    { sizeX: 3, sizeY: 3, row: 4, col: 3 },

  ];
  $scope.gridsterOpts = {
      columns: 6, // the width of the grid, in columns
      pushing: true, // whether to push other items out of the way on move or resize
      floating: true, // whether to automatically float items up so they stack (you can temporarily disable if you are adding unsorted items with ng-repeat)
      swapping: true, // whether or not to have items of the same size switch places instead of pushing down if they are the same size
      width: 'auto', // can be an integer or 'auto'. 'auto' scales gridster to be the full width of its containing element
      colWidth: 'auto', // can be an integer or 'auto'.  'auto' uses the pixel width of the element divided by 'columns'
      rowHeight: 'match', // can be an integer or 'match'.  Match uses the colWidth, giving you square widgets.
      margins: [10, 10], // the pixel distance between each widget
      outerMargin: true, // whether margins apply to outer edges of the grid
      sparse: false, // "true" can increase performance of dragging and resizing for big grid (e.g. 20x50)
      isMobile: false, // stacks the grid items if true
      mobileBreakPoint: 600, // if the screen is not wider that this, remove the grid layout and stack the items
      mobileModeEnabled: true, // whether or not to toggle mobile mode when screen width is less than mobileBreakPoint
      minColumns: 1, // the minimum columns the grid must have
      minRows: 2, // the minimum height of the grid, in rows
      maxRows: 100,
      defaultSizeX: 2, // the default width of a gridster item, if not specifed
      defaultSizeY: 1, // the default height of a gridster item, if not specified
      minSizeX: 1, // minimum column width of an item
      maxSizeX: null, // maximum column width of an item
      minSizeY: 1, // minumum row height of an item
      maxSizeY: null, // maximum row height of an item
      resizable: {
         enabled: true,
         handles: ['n', 'e', 's', 'w', 'ne', 'se', 'sw', 'nw'],
         start: function(event, $element, widget) {}, // optional callback fired when resize is started,
         resize: function(event, $element, widget) {}, // optional callback fired when item is resized,
         stop: function(event, $element, widget) {} // optional callback fired when item is finished resizing
      },
      draggable: {
         enabled: true, // whether dragging items is supported
        //  handle: '.my-class', // optional selector for drag handle
         start: function(event, $element, widget) {}, // optional callback fired when drag is started,
         drag: function(event, $element, widget) {}, // optional callback fired when item is moved,
         stop: function(event, $element, widget) {} // optional callback fired when item is finished dragging
      }
  };

    }]);

   app.config(AppConfig);
    AppConfig.$inject = ['$stateProvider', '$urlRouterProvider'];
    function AppConfig($stateProvider, $urlRouterProvider){

    	$urlRouterProvider.otherwise('/dashboard');

    	$stateProvider.state('dashboard', {
			url: '/dashboard',
			views: {
				'template1': {
					templateUrl: 'templates/template1.html',
					controller: 'template1Controller'
				}, 
				'template2': {
					templateUrl: 'templates/template2.html',
					controller: 'template2Controller'
				}, 
				'template3': {
					templateUrl: 'templates/template3.html',
					controller: 'template3Controller'
				}, 
				'template4': {
					templateUrl: 'templates/template4.html',
					controller: 'template4Controller'
				}, 
				'template5': {
					templateUrl: 'templates/template5.html',
					controller: 'template5Controller'
				}
			}
		})
    }

    // Controller
    app.controller('template1Controller', template1Controller);
    app.controller('template2Controller', template2Controller);
    app.controller('template3Controller', template3Controller);
    app.controller('template4Controller', template4Controller);
    app.controller('template5Controller', template5Controller);

    // templete 1
    template1Controller.$inject = ['$scope', '$scope', '$http'];
    function template1Controller($scope,$rootScope,  $http){
      // var user_api = localStorage.getItem('api')
    // url = user_api + 'appointment/receptionpending/'
    // $http.get(url)
        $http.get('https://1923612f6b8c.ngrok.io/students/birthday/')
        .then(function (response) {
            $scope.employees = response.data;
            console.log($scope.employees)
            console.log($scope.employees)
        })    
    }

    // template 2
      template2Controller.$inject = ['$scope', '$http'];
      function template2Controller($scope, $http){
        var data = {
          semister: '3', 
          course: 'B.tech', 
          day: 'Monday',
          branch: 'CO', 
        }
        $http.post("https://1923612f6b8c.ngrok.io/time/table/", JSON.stringify(data))
        .then(function (response) {
          $scope.employees = response.data;
            console.log(response);
            console.log(response.data);
                   })
            // console.log(c);
    // })
      }
    
    // template 3
    template3Controller.$inject = ['$scope', '$scope'];
    function template3Controller($scope, $http){

    console.log('wee')
      $scope.custom = {
        url: "http://www.google.com/calendar/feeds/indian__en%40holiday.calendar.google.com/public/basic",
        // className: 'gcal-event',           // an option!,
        currentTimezone: 'India', // an option!
        googleCalendarApiKey: 'AIzaSyCc5LZyMQ2pBB1dAJerfliEEu0P8hMUVwg'
    };

    $scope.eventSources = [$scope.custom];
    /* config object */
      $scope.uiConfig = {
        calendar:{
          height: 600,
          editable: false,
          header:{
            // left: 'month basicWeek basicDay agendaWeek agendaDay',
            left: 'title',
            center: '',
            right: 'today prev,next'
          },
          eventClick: $scope.alertEventOnClick,
          eventDrop: $scope.alertOnDrop,
          eventResize: $scope.alertOnResize
        }
      };





  }

    // template 4
    template4Controller.$inject = ['$scope', '$http'];
    function template4Controller($scope, $http){
      var data = {
        student_id: '1', 
      }
      $http.post("https://1923612f6b8c.ngrok.io/attendence/daily/", JSON.stringify(data))
      .then(function (response) {
        $scope.employees = response.data;
          console.log(response);
          console.log(response.data);
          var plogindata = JSON.parse(JSON.stringify(response.data));
          var data = JSON.stringify(plogindata);
          localStorage.setItem("patient_profile", data);
        })
          // console.log(c);
  // })
    }

    // template 5
    template5Controller.$inject = ['$scope', '$scope'];
    function template5Controller($scope, $http){
      
    }




  
			