<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="">
        <title>Guest Book</title>
        <link href="{{ url_for('static',filename='css/bootstrap.min.css') }}" rel="stylesheet">
        <link href="{{ url_for('static',filename='css/bootstrap-theme.min.css') }}" rel="stylesheet">
        <link href="{{ url_for('static',filename='css/theme.css') }}" rel="stylesheet">
    </head>
    <body>
        <div class="container theme-showcase" role="main">
            <div class="jumbotron">
                <h1>Guest Book</h1>
                <a type="button" class="btn btn-link" href="{{ url_for('sign') }}">Sign the Guest Book</a>
            </div>
            <div class="page-header">
                <h1>Name</h1>
            </div>
            <div class="well">
                <p>Lorem ipsum dolor sit amt, consectetur adipiscing elit. Maecenas sed diam eget risus varius blandit sit amt non 
                magna. Lorem ipsum dolor sit amt, consectetur adipiscing elit. Praesent commodo cursus magna, vel scelerisque nisl 
                consectetur et. Cras mattis consectetur purus sit amt fermentum. Duis mollis, est non commodo luctus, nisi erat 
                porttitor ligula, eget lacinia odio sem nec elit. Aenean lacinia bibendum nulla sed consectetur.</p>
            </div>
        </div>
    </body>
</html>