<h1>title</h1>
<p>Welcome to title</p>

<form action='/' method='POST'>
    <input name='url' />
    <input type='submit' />
</form>

<ul>
% for url in urls:
<li><a href="url/{{url['short']}}">url/{{url['short']}}</a></li>
% end
</ul>
