<?php
class Model_model extends CI_Model{
    function showimport($arr){
        $this->db->select('$tablename.*');
        $this->db->from('$tablename');
        foreach($arr as $key=>$val){
            $this->db->where($key,$val);
        }
        $query = $this->db->get();
        return $query;
    }
    function deleteimport($arr){
        foreach($arr as $key=>$val){
            $this->db->where('client_id', $id);
            $this->db->delete('client');
        }
    }
    function insertimport($arr){
        $query = $this->db->insert('$tablename',$arr);
        $id = $this->db->insert_id();        
        return $id;    
    }
    function updateimport($arr){
        $this->db->where('$primarykey',$arr['$primarykey']);
        $this->db->update('$tablename',$arr);
        return $arr['primarykey'];
    }
    function editimport($arr){
        $this->db->select('$tablename.*');
        $this->db->from('$tablename');
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