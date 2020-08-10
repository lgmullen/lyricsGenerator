import gpt_2_simple as gpt2

gpt2.download_gpt2()   # model is saved into current directory under /models/124M/
print("Starting")
sess = gpt2.start_tf_sess()
gpt2.finetune(sess, 'lyrics/lil uzi vert.txt', steps=10)   # steps is max number of training steps

gpt2.generate(sess)