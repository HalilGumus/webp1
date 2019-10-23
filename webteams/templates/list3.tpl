## coding: utf-8
<!DOCTYPE html>
<html>
    <head>
        <title>Web-Teams</title>
        <meta charset="UTF-8" />
        <script type='text/javascript' src='webteams.js'></script>

    </head>
    <body>
            % for key_s in data_o:
            <ul>
                <li><td>${data_o[key_s][0]}</td>
                <td>${data_o[key_s][1]}</td>
                <td>${data_o[key_s][2]}</td>
                <td>${data_o[key_s][3]}</td></li>
                <li><td>${data_o[key_s][4]}</td>
                <td>${data_o[key_s][5]}</td>
                <td>${data_o[key_s][6]}</td>
                <td>${data_o[key_s][7]}</td></li>
                <td>
                <a href="/edit/${key_s}">bearbeiten</a>
                <a href="/delete/${key_s}" class='clDelete'>löschen</a>
                </td>
            </ul>
            % endfor
        <div>
            <a href="/add">erfassen</a>
            <a href="/changeForm?listForm=aufzaehlung">Darstellung ändern</a>
        </div>
    </body>
</html>