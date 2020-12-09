print ('<label class="col-md-2 control-label" for="textinput">Pembekal: *</label>')
print ('<div class="col-md-4">')
print ('    <div class="input-group">')
print ('        <input class="required form-control" type="text" size="40" value="<? if(isset($rs_supplier)){ echo $rs_supplier->supplier_name;}?>" readonly id="supplier_name" name="supplier_name" />                                     ')
print ('        <span class="input-group-addon">')
print ('            <a href="javascript:void(null);" onClick="openSupplier();"><? echo img('/'img/zoom16.png'/')?></a>')
print ('        </span>')
print ('        <input type="hidden" id="supplier_id" value="<? if(isset($rs_supplier)){ echo $rs_supplier->supplier_id;}?>" name="supplier_id">')
print ('    </div>')
print ('</div>')


