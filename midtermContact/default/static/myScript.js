


function check(){

　　var myforms=document.forms;

　　var mypasswd=myforms[0].password1.value;
　　var myReg=/^[a-zA-Z0-9]\w{6,16}$/;
 
　　if(myReg.test(mypasswd)){
　　　　pswdnt.innerText="";
　　　　return true;
　　}else{
　　　　pswdnt.innerText="请输入字母数字组合6-16位密码";
　　　　return false;
	}
}

function checkSearch(){
	var myforms=document.forms;
	var namelen=myforms[0].name.value.length;

	if(namelen > 0){
		nament.innerText="";
		return true;
	}else{
		nament.innerText="请输入姓名";
		return false;
	}
}

function listen_name(){
　　var myforms=document.forms;
	var x = myforms[0].fname.value;
	namec.innerText=x;
}


function checkNewContect(){

　	var myforms=document.forms;


	var mytel=myforms[0].tel.value;
	var myemail=myforms[0].email.value;

	var myQQ=myforms[0].QQnum.value;
	var namelen=myforms[0].name.value.length;
	var	addrlen=myforms[0].addr.value.length;
　	var myRegTel=/^((0\d{2,3}-\d{7,8})|(1\d{10}))$/;
 	var myRegEmail=/^[a-zA-Z0-9_-]+@([a-zA-Z0-9]+\.)+(com|cn|net|org)$/;

  	var myRegQQ=/^[1-9][0-9]\w{4,12}$/; 		
 	
　　if(myRegTel.test(mytel)){
　　　　telnt.innerText="";
　　　　
　　}else{
　　　　telnt.innerText="请输入正确的电话号码";
　　　　return false;
	}
	
　　if(myRegEmail.test(myemail)){
　　　　emailnt.innerText="";
　　　　
　　}else{
　　　　emailnt.innerText="请输入正确的电子邮箱";
　　　　return false;
	}

　　if(myRegQQ.test(myQQ)){
　　　　QQnt.innerText="";
　　　　
　　}else{
　　　　QQnt.innerText="请输入6-11位数字";
　　　　return false;
	}
	
　　if(namelen > 0){
　　　　nament.innerText="";
　　　　
　　}else{
　　　　nament.innerText="请输入姓名";
　　　　return false;
	}	
	
　　if(addrlen > 0){
　　　　addrnt.innerText="";
　　　　
　　}else{
　　　　addrnt.innerText="请输入地址";
　　　　return false;
	}	
	
	return true;
	
}

$().ready(function() {
    $("#commentForm").validate();
});