This is a simulation of oscilloscope. It shows how two different sine waves are combined to produce the Lissajous figures. 

# Instructions to run simulation

[Note: these instructions are for Windows users taken from [manim documentation](https://docs.manim.community/en/stable/installation/uv.html).]

## Installing necessary softwares

### uv (Package Manager)

Open Terminal and run(`ctrl+v` then `enter`) the following: 
 
`powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

### Python (Interpreter)

`uv python install`

### MikTeX (Displays Equations and Mathematical Texts)

Go to https://miktex.org/download and download and run the installer. 

### Git (Github Repositories Manager)

Download and install from https://gitforwindows.org/

### VSCode (IDE)

[Note: This one is recommended, but there are ways you can modify the code and simulate it without using VSCode .]

From https://code.visualstudio.com/download, download and run installer. 

After completing installation, go to 'Extensions' in the IDE and install `Python` by Microsoft. 

## Simulating

### Clone Git Repository

Run the following command in terminal to download the code: 

```
cd Downloads
mkdir Manimimations
cd Manimations
git clone https://github.com/BayezidBostami06/Lissajous.git
```

### Setting up VSCode

Open the project folder in VSCode. Press `` Ctrl+Shift+` `` to run the terminal **inside VSCode**. 

Now run `uv run manim checkhealth` to check if everything is working properly. You should see the following message once you run the command: 

```
No problems detected, your installation seems healthy!
Would you like to render and preview a test scene? [y/N]:
```

Enter `y` to see the manimation of the logo of manim. Feel free to enter `n` if you don't want to.

### Editing Code

Open `main.py` and scroll down to the bottom. Call the Play() function with arguments t=(Time of simulation), A = [A1, A2] (Amplitudes), f = [f1, f2] (frequencies), delta_phi = (Phase difference in degrees)

### Running code

In the terminal **inside VSCode**, run the following command: 
`manim main.py DynamicOscilloscope --disable_caching -p`

The video will autostart once the rendering is completed. You can also access the videos from `./media/videos/1080p60`.