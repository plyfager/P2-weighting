torchrun scripts/image_train.py \
--data_dir /data/images --attention_resolutions 16 \
--class_cond False --diffusion_steps 1000 \
--dropout 0.0 --image_size 256 --learn_sigma True \
--noise_schedule linear --num_channels 128 --num_head_channels 64 \
--num_res_blocks 1 --resblock_updown True --use_fp16 False \
--use_scale_shift_norm True --lr 2e-5 --batch_size 8 \
--rescale_learned_sigmas True --p2_gamma 1 --p2_k 1 \
--log_dir logs --batch_size 8 \
--load_checkpoint ~/Downloads/ffhq_baseline.pt
# --save_interval 1 