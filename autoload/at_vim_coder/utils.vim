let s:save_cpo = &cpo
set cpo&vim

function! at_vim_coder#utils#echo_message(msg)
	echo '[at-vim-coder] ' . a:msg
endfunction

function! at_vim_coder#utils#echo_err_msg(msg)
	echo '[at-vim-coder] Error Occurred'
	echo a:msg
endfunction

let &cpo = s:save_cpo
unlet s:save_cpo
