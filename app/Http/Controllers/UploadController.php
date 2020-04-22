<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;
use Illuminate\Support\Facades\Redis;
// use Illuminate\Support\Facades\Redis;


class UploadController extends Controller
{
	public function upload(){
		return view('upload');
	}
   private function printFile($file){
      	        // nama file
		echo 'File Name: '.$file->getClientOriginalName();
		echo '<br>';

      	        // ekstensi file
		echo 'File Extension: '.$file->getClientOriginalExtension();
		echo '<br>';

      	        // real path
		echo 'File Real Path: '.$file->getRealPath();
		echo '<br>';

      	        // ukuran file
		echo 'File Size: '.$file->getSize();
		echo '<br>';

      	        // tipe mime
      echo 'File Mime Type: '.$file->getMimeType();
      echo '<br>';

      	        // isi dengan nama folder tempat kemana file diupload
		$tujuan_upload = 'nihmasuk';
   }

	public function proses_upload(Request $request){
      $redis = Redis::connection();
		$this->validate($request, [
			'attachment' => 'required',
         'keyword' => 'required',
         'algoritma' => 'required'
		]);

		// menyimpan data file yang diupload ke variabel $file
      // $file = $request->file('file');
      $files = $request->file('attachment');
      $algo = $request->input('algoritma');
      $milliseconds = round(microtime(true) * 1000);
      $filenames = [];
      if($request->hasFile('attachment'))
      {
         foreach ($files as $file) {
            // $this->printFile($file);
            // $file_path = $file.move('/files/'.$file->$file->getClientOriginalName());
            $file_path = 'files/'.$milliseconds.'/';
            $file->move($file_path,$file->getClientOriginalName());
            array_push($filenames,$file_path.$file->getClientOriginalName());
         }
      }
      $keyword = $request->input('keyword');

      $data_masukan = [
         "filenames" => $filenames,
         "keyword" => $keyword,
         "algo" => $algo,
         "result" => []
      ];
      $data_masukan = json_encode($data_masukan);
      // echo $data_masukan;
      $redis->set($milliseconds,$data_masukan);
      $process = new Process(['python3', 'main.py',$milliseconds]);
      $process->run();
      sleep(3);
      echo '<br/>';
      $results = $redis->get($milliseconds);
      // executes after the command finishes
      if (!$process->isSuccessful()) {
         throw new ProcessFailedException($process);
      }
      return view('result',["keyword"=>$keyword, "results"=>$results]);
	}
}