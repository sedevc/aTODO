
<html>
	<head>
		<link href='http://fonts.googleapis.com/css?family=Roboto+Slab:100,300' rel='stylesheet' type='text/css'>
		<style type="text/css">
		body{
			font-family: 'Roboto Slab', serif;
			font-size: 13px;
		}		
		.container{
			padding: 20px;
			margin: 20px;
			height: 300px;
			width: 500px;
			background-color: #f1f1f1;
			overflow-y: scroll;
		}
		.main_table{
			border: 1px solid black;
			width: 470px;
		}
		#task{
			font-size: 12px;
		}
		#rownumber{
			width: 20px;
			font-size: 12px;
			font-style: bold;
		}

		</style>
	</head>
<body>
	<div class="container">
		<table class="main_table">
			%for index, row in enumerate(rows):
				<tr>
					
					<td width="20px"><a href="remove/{{row[0]}}"><img src="http://www.uaa.alaska.edu/templates/DenaliView/images/icons/redexmark.gif" width="15px" height="15px"></a></td>
					<td width="20px"><a href="edit/{{row[0]}}"><img src="https://cdn3.iconfinder.com/data/icons/interaction-design/512/Edit_A-512.png" width="15px" height="15px"></a></td>
					<td id="rownumber">{{index+1}}:</td>
					<td id="task">{{row[2]}}</td>
					%if row[1]:
						<td><img src="https://cdn2.iconfinder.com/data/icons/toolbar-signs-2/512/ok_check_yes_tick_accept_success-512.png" width="15px" height="15px"/></td>
					%else:
						<td><img src="" width="15px" height="15px"></td>
					%end
				</tr>
			%end
		</table>
		<p>Add a new task to the ToDo list:</p>
		<form action="/new" method="GET">
			<textarea rows="4" cols="50" name="task" maxlength="60">Enter your todo..</textarea>
			<br>
			<select name="status">
			<option>open</option>
			<option>closed</option>
			</select>
			
			<input type="submit" name="save" value="OK">
		</form>
	</div>

</body>
</html>