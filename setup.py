import os
# append env dirs of conda
os.system("conda config --append envs_dirs /scratch/as14229/envs_dirs/ ")
# set alias for Data directory
os.system('echo "SuperGAN_DATA=\'cd /home/as14229/Shared/SuperGAN/data/\'" >> ~/.bashrc')
# set alias for activation
os.system('echo "alias GAN=\'conda activate GAN\'" >> ~/.bashrc')

print("\nEnvironment Imported - Use 'GAN' to activate\n")
