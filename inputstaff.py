print ('<div class="form-group col-md-12">')
print ('    <label class="col-md-2 control-label" for="textinput">Nama *</label>')
print ('     <div class="col-md-4">')
print ('            <div class="input-group">')
print ('                <input type="text" class="required form-control" size="50" readonly value="<? if(isset($rs_incharge)){ echo $rs_incharge->staff_name;} ?>" ')
print ('                id="incharge_name" name="incharge_name" size="30" />')
print ('                <span class="input-group-addon">')
print ('                    <a href="javascript:void(null);" onClick="openIncharge();"><? echo img(images/user_male.png)?></a>')
print ('                </span>')
print ('            </div>')
print ('    </div>')
print ('</div>')
