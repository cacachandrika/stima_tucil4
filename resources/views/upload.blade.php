<!DOCTYPE html>
<html>
<head>
	<title>13518001 | Chandrika Azharyanti</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

</head>
<body>
	<!-- <div class="row"> -->
		<!-- <div class="container"> -->
			<h1 class="text-center my-3">My InfoExtraction App</h1>
			
			<div class="col-lg-5 mx-auto my-5">	

				<!-- @if(count($errors) > 0)
				<div class="alert alert-danger">
					@foreach ($errors->all() as $error)
					{{ $error }} <br/>
					@endforeach
				</div>
				@endif -->

				<form action="/uploaddone" method="POST" enctype="multipart/form-data">
					{{ csrf_field() }}

					<div class="form-group">
                  <b>Masukkan File</b><br/>
                  <input type="file" name="attachment[]" multiple="multiple">
					</div>

					<div class="form-group">
						<b>Keyword</b>
						<textarea class="form-control" name="keyword"></textarea>
					</div>

               <input type="radio" id="Boyer-Moore" name="algoritma" value="Boyer-Moore">
               <label for="Boyer-Moore">Boyer-Moore</label><br>
               <input type="radio" id="KMP" name="algoritma" value="KMP">
               <label for="KMP">KMP</label><br>
               <input type="radio" id="Regex" name="algoritma" value="Regex">
               <label for="Regex">Regex</label>
               <br/>

					<input type="submit" value="cari" class="btn btn-primary">
               <br/>
               <br/>
               <br/>
               <b>----------------------------------------------------------------------</b>
               <div class="links">
                    <a href="perihal.html">perihal</a>
                </div>
				</form>
			</div>
		<!-- </div> -->
	<!-- </div> -->
</body>
</html>