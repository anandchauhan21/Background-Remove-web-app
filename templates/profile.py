<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Profile</title>
</head>

<body>
    <div class="bg-success p-2 text-dark bg-opacity-10">
        <h1>BACK-GROUND REMOVE</h1>
    </div>

	<hr class="border border-danger border-2 opacity-50">


    <div class="bg-success p-2 text-dark bg-opacity-10">
		<div class="row text-center" style="--bs-columns: 4">
		    <div class="col">
			    <h2>Before</h2>
		    </div>
		    <div class="col">
			    <h2>After</h2>
		    </div>
	    </div>
    </div>
	<br>
	<div class="row text-center" style="--bs-columns: 4">
        <div class="col">
			<img src="{{ before }}" alt="before">
		</div>
		<div class="col">
			<img src="{{ user_image }}" alt="User Image">
		</div>
	</div>
<br>

	<form action = "/" method = "GET"
         enctype = "multipart/form-data">
			 <div class="col col-md-4">
				 <input type = "submit" class="btn btn-outline-success" value="GoBack"/>

			 </div>
		 </div>
      </form>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</body>
</html>
