"""
Helpers for distributed training.
"""

import io
import os
import socket

import blobfile as bf
# from mpi4py import MPI
import torch as th
import torch.distributed as dist

# Change this to reflect your cluster layout.
# The GPU for a given rank is (rank % GPUS_PER_NODE).
GPUS_PER_NODE = 8

SETUP_RETRY_COUNT = 3

def setup_dist():
    env_dict = {
        key: os.environ[key]
        for key in ("MASTER_ADDR", "MASTER_PORT", "RANK", "WORLD_SIZE")
    }
    print(f"[{os.getpid()}] Initializing process group with: {env_dict}")  
    dist.init_process_group(backend="nccl")
    


# # def load_state_dict(path, **kwargs):
# #     """
# #     Load a PyTorch file without redundant fetches across MPI ranks.
# #     """
# #     chunk_size = 2 ** 30  # MPI has a relatively small size limit
# #     if dist.get_rank() == 0:
# #         with bf.BlobFile(path, "rb") as f:
# #             data = f.read()
# #         num_chunks = len(data) // chunk_size
# #         if len(data) % chunk_size:
# #             num_chunks += 1
# #         dist.broadcast(num_chunks, 0)
# #         for i in range(0, len(data), chunk_size):
# #             dist.broadcast(data[i : i + chunk_size], 0)
# #     else:
# #         num_chunks = dist.broadcast(None, 0)
# #         data = bytes()
# #         for _ in range(num_chunks):
# #             data += dist.broadcast(None, 0)

# #     return th.load(io.BytesIO(data), **kwargs)


# def sync_params(params):
#     """
#     Synchronize a sequence of Tensors across ranks from rank 0.
#     """
#     for p in params:
#         with th.no_grad():
#             dist.broadcast(p, 0)


# def _find_free_port():
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.bind(("", 0))
#         s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         return s.getsockname()[1]
#     finally:
#         s.close()
