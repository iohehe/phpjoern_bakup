--TEST--
Nop statements
--FILE--
<?php

require __DIR__ . '/../util.php';

$code = <<<'PHP'
<?php
$a;
;
$b;
PHP;

echo ast_dump(ast\parse_code($code, $version=30)), "\n";
echo ast_dump(ast\parse_code($code, $version=40)), "\n";

?>
--EXPECT--
AST_STMT_LIST
    0: AST_VAR
        name: "a"
    1: null
    2: AST_VAR
        name: "b"
AST_STMT_LIST
    0: AST_VAR
        name: "a"
    1: AST_VAR
        name: "b"
