$(function(){
$("#button").click(function() {
  submit($('input').val());
});
$("form").submit(function(){
    submit($('input').val());
});
});

function submit (s)
{
    $.get( "/analysis/"+s, function( data ) {
	$("#loading").text("");
	var bet = data.split("|||");
        var text = bet[0];
	var text2 = bet[1];
var res = text.split(" ");
console.log(res+"");
if(res.length==0)
{
	$("#harmful").text("No bad tweets!");
	
}
else
{
	console.log("hello");
	$("#harmful").text("Consider deleting the following tweets");
}
var res2 = text2.split(" ");
if(res2.length==0)
{
	console.log(0);
	$("#haha").text("You don't follow any bullies!");
}
else
{
	console.log("hello");
	$("#haha").text("Consider unfollowing these potential bullies");
}
for(var i = 0; i < res.length; i++)
    {
        $("#wow").append('<blockquote class="twitter-tweet" data-lang="en"><a href="'+res[i]+'"></a></blockquote><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script><a href="'+res[i]+'"><button class="waves-effect waves-light btn blue accent-2" type="button">Delete tweet</button></a>')
    }
    

for(var i = 0; i < res2.length; i++)
    {
	var testing = res2[i].substring(res2[i].indexOf('.com')+5,res2[i].indexOf('/status'));
	testing = "https://twitter.com/" + testing;
        $("#wow2").append('<blockquote class="twitter-tweet" data-lang="en"><a href="'+res2[i]+'"></a></blockquote><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script><a href="'+testing+'"><button class="waves-effect waves-light btn blue accent-2" type="button">Unfollow</button></a>')
    }
    });
    $("#center").animate({marginTop: '21%'},  {duartion: 50, queue: true});
    $("#center").animate({marginTop: '-100%', marginBottom: '0'},  {duartion: 500, queue: true});
    $("#center2").animate({marginTop: '85%'},  {duartion: 500, queue: true});
    $("*").css("overflow", "auto");
    $("#good").text(s);
    
    
}
