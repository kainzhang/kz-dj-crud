days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
function ymd()
{
	for(var i=2010; i<=2019; i++)
		document.thisform.YY.options.add(new Option(i, i));
	for(var i=1; i<13; i++)
		document.thisform.MM.options.add(new Option(i, i));
	var m = document.thisform.MM.options[document.thisform.MM.selectedIndex].value;
	if(m) mnd(m);
}

if(window.attachEvent)
	window.attachEvent("onload", ymd);
else
	window.addEventListener('load', ymd, false);

function ynd(year)
{
	var m = document.thisform.MM.options[document.thisform.MM.selectedIndex].value;
	if( m == "MM"){
		document.thisform.DD.options.length = 1;
	} else {
		var d = days[m];
		if( m == 2 && isleap(year)) d++;
		getd(d);
	}
}

function mnd(month)
{
	var y = document.thisform.YY.options[document.thisform.YY.selectedIndex].value;
	if( y == "YY"){
		document.thisform.DD.options.length = 1;
	} else {
		var d = days[month];
		if( month == 2 && isleap(y)) d++;
		getd(d);
	}
}

function isleap(n)  {
    return(n%4==0 && n%100!=0 || n%400==0);
}

function getd(d)
{
	var t = document.thisform.DD;
	t.options.length = 1;
	for(i=1; i<=d; i++)
		t.options.add(new Option(i, i));
}