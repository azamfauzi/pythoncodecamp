<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Jobtype extends CI_Controller {
  
	function index(){
		//$arrSess = $this->auth->get_session();
		//$arrSess['iduser'] = $arrSess['userid'];
		$data1['menu'] = 'job';
		$this->load->view('header',$data1);
		$this->load->view('sidebar',$arrSess);
		$data['title'] = 'Create New User';
		$this->load->view('footer');
	}
	function create($id=0){
		$data1['menu'] = 'job';
		if($id > 0){
			$data['title'] = 'Edit Job Type';
		}else{
			$data['title'] = 'Create Job Type';
		}		
		if($id > 0){
			$this->load->model('jobtype_model','jobtype');
			$data['row'] = $this->jobtype->showjobtype($mod)->row();
			$this->load->model('global_model','global');
			if($this->global->is_exist('jobreport','client_id',$id) == true){
				$data['disablezone'] = 'Y';
			}
		}		
		$data['content'] = 'jobtypecreate';
		$this->load->view('layout',$data);
		
	}
	function save(){
		$data1['menu'] = 'job';	
		$this->load->model('jobtype_model','jobtype');
		$data['title'] = 'Update Record';		
        $data['content'] = 'jobtypecreate';      
          
        if(isset($arr['jobtype_id']) && $arr['jobtype_id'] > 0){            
            $this->jobtype->updatejobtype($arr);
        }else{
            $this->jobtype->insertjobtype($arr);
        }
		redirect('/jobtype/view/', 'refresh');		
	
	}
	function view(){		
		$data1['menu'] = 'job';		
		$data['title'] = 'jobtype List';
		$this->load->model('Jobtype_model','jobtype');
        $data['query'] = $this->model->showjobtype();
		$data['content'] = 'jobtype';
        $this->load->view('layout',$data);
        
	}
	function delete($id){

        $this->load->model('jobtype_model','jobtype');
		$this->load->model('global_model','global');
		$this->jobtype->deletejobtype(array('jobtype_id'=>$id));        
		redirect('/jobtype/create/', 'refresh');

	}
	
	
}
?>