U
     �;a�  �                   @   s   d d� Z dS )c           
      C   s�   g }t | �}d}|s�d}td|�D ]X}||kr"d}td|�D ],}||kr<||kr<| | | dkr<|d }q<||kr"|}|}q"|dkr�d}q|�|� qdgt | � }	|g kr�d|	|d < |dd � }q�|	S )NF�    �   T)�len�range�append)
Zinput_graphZsol�top�finishedZmaximum�i�val�jZverticeZnodes� r   �vertex_cover.py�solve_vc   s,     
r   N)r   r   r   r   r   �<module>   �    