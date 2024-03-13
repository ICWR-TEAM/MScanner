<?php

$blacklist = file_get_contents("blacklist.txt");
$explode_blacklist = explode("\n", $blacklist);

class Main {

    public function __construct($Target) {
        $this->res_dir = array($Target); //result
        $this->scan_directory($Target);
        $result = $this->get_file($this->res_dir, explode_blacklist);
        $this->proc($result);
    }

    public function proc($datas) {
        foreach ($datas as $data) {
            echo $data["file"] . "\n";
        }
    }

    public function scan_directory($directory) {
        $files = scandir($directory);
        foreach ($files as $file) {
            $item_path = $directory . '/' . $file;
            if (is_dir($item_path) && $file != '.' && $file != '..') {
                $this->res_dir[] = $item_path;
                $this->scan_directory($item_path);
            }
        }
    }

    public function get_file($paths, $suspect_code) {
        $result = array();
        foreach ($paths as $path) {
            $files = scandir($path);
            foreach ($files as $file) {
                $item_path = $path . '/' . $file;
                if (is_file($item_path)) {
                    $op_file = file_get_contents($item_path);
                    $pattern_suspect_code = '/\b(' . implode('|', array_map('preg_quote', $suspect_code)) . ')\b/';
                    preg_match_all($pattern_suspect_code, $op_file, $matches);
                    if (!empty($matches[0])) {
                        foreach ($matches[0] as $match) {
                            $result[] = array("file" => $item_path);
                            break; // Stop after finding the first match
                        }
                    }
                }
            }
        }
        return $result;
    }
}

new Main("target");

?>
