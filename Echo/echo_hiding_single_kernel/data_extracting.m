close all; clear all; clc;

audio = audioload();

file = 'conf.txt';
fid  = fopen(file, 'r');
text = fread(fid,'*char')';
fclose(fid);

msg = echo_dec(audio.data);
fprintf('%s\n', msg);