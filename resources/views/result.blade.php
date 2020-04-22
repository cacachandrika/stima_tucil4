<!DOCTYPE html>
<html>
<head>
	<title>result page</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

</head>
<body>

<h3>Hasil pencarian :</h3>
<h3>Keyword: {{$keyword}} </h3>
@foreach(json_decode($results,true)["result"] as $result)
<div class="list-group">
<a href="#" class="list-group-item list-group-item-action flex-column align-items-start">
    <p>jumlah: {{$result["jumlah"]}} waktu: {{$result["date"]}} {{$result["time"]}} </p>
    <h5 class="mb-1">Kalimat: {{$result["kalimat"]}}</h5>
    <?php $nama = basename($result["filename"]); ?>
    <small>nama file: {{$nama}}</small>
</a>
</div>
@endforeach

</body>