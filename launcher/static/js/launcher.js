function startApp(computer, app){
    $.post("action/", { computer:computer, action: 'run', app:app } ,function(data){
	    $("#"+computer+".*").removeClass("selected");
	    $("#"+computer+"."+app).addClass("selected");
        });
}

function stopPrograms(computer, app){
    $.post("action/", { computer:computer, action: 'stop', app:app} ,function(data){
	    $("#"+computer+".*").removeClass("selected");
	    $("#"+computer+"."+app).addClass("selected");
        });
}