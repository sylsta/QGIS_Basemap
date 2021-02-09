<?php

// Réaffiche le contenu de <body>
$racine = simplexml_load_file(‘QGIS_WFS.xml’);
$body = $racine->body;
//foreach(body->children() as $nom=>$element){
//    echo "La balise $nom contient l’élément \ » », utf8_decode($element), ‘"<br>’;
//}
echo "coucou";
?>