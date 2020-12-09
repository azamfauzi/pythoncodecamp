<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class ControllerName extends CI_Controller {
  
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
			$data['title'] = 'Edit $title';
		}else{
			$data['title'] = 'Create $title';
		}		
		if($id > 0){
			$this->load->model('$model_model','$model');
			$data['row'] = $this->model->showModel($mod)->row();
			$this->load->model('global_model','global');
			if($this->global->is_exist('jobreport','client_id',$id) == true){
				$data['disablezone'] = 'Y';
			}
		}		
		$data['content'] = '$classcreate';
		$this->load->view('layout',$data);
		//$this->load->view('blogview', $data);
		//$this->load->view('footer');
	}
	function save(){
		$data1['menu'] = 'job';	
		$this->load->model('$model_model','$model');
		$data['title'] = 'Update Record';		
        $data['content'] = '$classcreate';
        
        if(isset($arr['$primarykey']) && $arr['$primarykey'] > 0){            
            $this->model->updatemodel($arr);
        }else{
            $this->model->insertmodel($arr);
        }
		redirect('/$class/view/', 'refresh');
		
	//	$this->load->view('footer');
	}
	function view(){		
		$data1['menu'] = 'job';		
		$data['title'] = '$class List';
		$this->load->model('$Model_model','$model');
        $data['query'] = $this->model->showModel();
		$data['content'] = '$classlist';
        $this->load->view('layout',$data);
        
	}
	function remove($id){
        $this->load->model('$Model_model','$model');
		$this->load->model('global_model','global');
		/*if($this->global->is_exist('jobreport','client_id',$id) == false){
			$this->job->delete_client($id);
        }
        */        
        $this->model->updatemodel($arr);        
		redirect('/$class/view/', 'refresh');
	}
	
	
}
?>