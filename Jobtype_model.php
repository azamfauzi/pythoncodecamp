<?php
class Jobtype_model extends CI_Model{
    function showJobType($arr){
        $this->db->select('l_jobtype.*');
        $this->db->from('l_jobtype');
        foreach($arr as $key=>$val){
            $this->db->where($key,$val);
        }
        $query = $this->db->get();
        return $query;
    }
    function deleteJobType($arr){
        foreach($arr as $key=>$val){
            $this->db->where('jobtype_id', $primarykey);
            $this->db->delete('l_jobtype');
        }
    }
    function insertJobType($arr){
        $query = $this->db->insert('l_jobtype',$arr);
        $id = $this->db->insert_id();        
        return $id;    
    }
    function updateJobType($arr){
        $this->db->where('jobtype_id',$arr['jobtype_id']);
        $this->db->update('l_jobtype',$arr);
        return $arr['jobtype_id'];
    }
    function editJobType($arr){
        $this->db->select('l_jobtype.*');
        $this->db->from('l_jobtype');
        if(!empty($arr)){
            foreach($arr as $key=>$val){
                $this->db->where($key,$val);
            }
        }
        $query = $this->db->get();
        return $query;
    }
}
?>