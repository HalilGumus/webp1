## coding: utf-8
<!DOCTYPE html>
<html>
    <head>
        <title>Web-Teams</title>
        <meta charset="UTF-8" />
        <script type='text/javascript' src='webteams.js'></script>
        <style>
            @import"/webteams.css";
        </style>
    </head>
    <body>
        <table>
            <tr>
                <th>Name (1)</th><th>Vorname (1)</th><th>Matr.-Nr. (1)</th><th>Semester (1)</th>
                <th>Name (2)</th><th>Vorname (2)</th><th>Matr.-Nr. (2)</th><th>Semester (2)</th><th>Aktion</th>

            </tr>
            % for key_s in data_o:
            <tr>
                <td>${data_o[key_s][0]}</td>
                <td>${data_o[key_s][1]}</td>
                <td>${data_o[key_s][2]}</td>
                <td>${data_o[key_s][3]}</td>
                <td>${data_o[key_s][4]}</td>
                <td>${data_o[key_s][5]}</td>
                <td>${data_o[key_s][6]}</td>
                <td>${data_o[key_s][7]}</td>
                <td>
                <a href="/edit/${key_s}">bearbeiten</a>
                <a href="/delete/${key_s}" class='clDelete'>löschen</a>
                </td>
            </tr>
            % endfor
        </table>
        <div>
            <a href="/add">erfassen</a>
            <a href="/changeForm?listForm=tabelle">Darstellung ändern</a>
        </div>
    </body>
</html>