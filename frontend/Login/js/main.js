var app = angular.module("myApp", []);
app.controller("loginController", function ($scope, $http) {
    $scope.mailId = null;
    $scope.password = null;

    $scope.btnlogin= function (mailId, password) {

        var data = {
            mailId: mailId,
            password: password
        }
        console.log(data);
        $http.post("https://1923612f6b8c.ngrok.io/student/login/", JSON.stringify(data))
            .then(function (res) {
                console.log(res);
                console.log(res.data);
                console.log(res.data);
                var docdata = JSON.stringify(res.data);
                console.log(docdata);
                window.location.href = "../index.html";
                alert('esf')
            })
    }
});