


function check(){

　　var myforms=document.forms;

　　var mypasswd=myforms[0].password1.value;
　　var myReg=/^[a-zA-Z0-9]\w{5,16}$/;



	var namelen=myforms[0].fname.value.length;

	if(namelen > 0){
		nament.innerText="";
		return true;
	}else{
		nament.innerText="请输入姓名";
		return false;
	}

　　if(myReg.test(mypasswd)){
　　　　pswdnt.innerText="";
　　　　return true;
　　}else{
　　　　pswdnt.innerText="请输入字母数字组合6-16位密码";
　　　　return false;
	}
}

function check_editpswd(){
	var myforms=document.forms;

	var mypasswd1=myforms[1].password1.value;
	var mypasswd2=myforms[1].password2.value;
	var myReg=/^[a-zA-Z0-9]\w{5,16}$/;
　　if(myReg.test(mypasswd1)){
　　　　pswdnt1.innerText="";
		if(mypasswd1==mypasswd2){
			return true;
		}else{
			pswdnt2.innerText="两次密码输入不同";
			return false;
		}


　　　　return true;
　　}else{
　　　　pswdnt1.innerText="请输入字母数字组合6-16位密码";
　　　　return false;
	}



}
function check_logup(){
	var myforms=document.forms;

	var mypasswd1=myforms[0].password1.value;
	var mypasswd2=myforms[0].password2.value;

	var namelen=myforms[0].fname.value.length;

	if(namelen > 0){
		nament.innerText="";

	}else{
		alert("请输入姓名");
		nament.innerText="请输入姓名";
		existname.innerText="";
		return false;
	}

	var myReg=/^[a-zA-Z0-9]\w{5,16}$/;

		existname.innerText="";
	　if(myReg.test(mypasswd1)){
　　　　pswdnt1.innerText="";
		if(mypasswd1==mypasswd2){
			return true;
		}else{
			alert("两次密码输入不同");
			pswdnt2.innerText="两次密码输入不同";

			return false;
		}


　　　　return true;
　　}else{
		alert("请输入字母数字组合6-16位密码");
		pswdnt1.innerText="";
　　　　pswdnt1.innerText="请输入字母数字组合6-16位密码";
　　　　return false;
	}



}


function checkSearch(){
	var myforms=document.forms;
	var Len=myforms[0].search.value.length;

	if(Len > 0){
		searchnt.innerText="";
		return true;
	}else{
		alert("请输入关键字");
		//questionnt.innerText="";
		//searchnt.innerText="请输入关键字";
		return false;
	}
}


function checkContent(){
	var myforms=document.forms;
	var Len=myforms[1].content.value.length;

	if(Len > 0){
		//searchnt.innerText="";
		return true;
	}else{
		alert("请输入回答");

		return false;
	}
}



function checkQuestion(){
	var myforms=document.forms;
	var Len=myforms[1].question.value.length;

	if(Len > 0){
		//questionnt.innerText="";
		return true;
	}else{
		alert("请输入问题");
		//searchnt.innerText="";
		//questionnt.innerText="请输入问题";
		return false;
	}
}




function listen_name(){
　　var myforms=document.forms;
	var x = myforms[0].fname.value;
	namec.innerText=x;
}


