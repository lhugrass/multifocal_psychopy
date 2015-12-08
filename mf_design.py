#This is a psychopy version of David's VPIXX multifocal stimulus that I've put together.
#You'll need to set window size for your monitor and make sure that you have the '40Patch_py_Q1.csv' saved on your computer
#We read the csv using pandas and then create variables based on the columns in the csv file. 
#You can play around a bit with the appearance of the stimulus. 
#Variables S1 - S6 can modify the size of patches in each ring and variables res1-res6 set the angular resolution
#The for-loop sets the contrast for each patch based on the values in the csv and updates each frame
#I've included code from the timebyframes psychopy example to add the ability to set the psychopy experiment runtime process priority
#and disable python garbage collection to see if either influences the precision of your frame flips. 
#The code generates some graphs at the end of the experiment

from psychopy import visual, core,logging, event, data  # import some libraries from PsychoPy=====
from psychopy.tools.filetools import fromFile
import gc, numpy,pylab, matplotlib,pandas as pd
visual.useFBO=True#if available (try without for comparison)


#create a window
mywin = visual.Window(size=(1280, 800), monitor="testMonitor", units="deg", colorSpace='rgb',fullscr=True, allowGUI=False, waitBlanking=True)
nIntervals = 4096 #set number of frames you wish to write 

#these bits of code set the runtime process priority 
visual.useFBO=False #if available (try without for comparison)
disable_gc = False
process_priority = 'high' # 'high' or 'realtime
if process_priority == 'normal':
    pass
elif process_priority == 'high':
    core.rush(True)
elif process_priority == 'realtime':
    # Only makes a diff compared to 'high' on Windows.
    core.rush(True, realtime = True)
else:
    print 'Invalid process priority:',process_priority,"Process running at normal."
    process_priority = 'normal'

if disable_gc:
    gc.disable()

#This code is for playing around with the patch size for each ring and the angular resolution. Note fewer frames are lost with lower res. 
#Note - keep in mind how many wedges there are on each ring when setting angular res to ensure that you don't end up with ugly gaps b/w wedges
s1=1 #size for the ring 1 patches (n=6)
s2=2 #size for the ring 2 patches (n=8)
s3=4 #size for the ring 3 patches (n=8)
s4=8 #size for the ring 4 patches (n=8)
s5=16#size for the ring 5 patches (n=6)
s6=32#size for the ring 6 patches (n=4)
res1=6
res2=8
res3=16
res4=16
res5=12
res6=16

# Setup section, read variable names from file
data = pd.read_csv('40Patch_py_Q1.csv') 
patches1=data['patch1']
patches2=data['patch2']
patches3=data['patch3']
patches4=data['patch4']
patches5=data['patch5']
patches6=data['patch6']
patches7=data['patch7']
patches8=data['patch8']
patches9=data['patch9']
patches10=data['patch10']
patches11=data['patch11']
patches12=data['patch12']
patches13=data['patch13']
patches14=data['patch14']
patches15=data['patch15']
patches16=data['patch16']
patches17=data['patch17']
patches18=data['patch18']
patches19=data['patch19']
patches20=data['patch20']
patches21=data['patch21']
patches22=data['patch22']
patches23=data['patch23']
patches24=data['patch24']
patches25=data['patch25']
patches26=data['patch26']
patches27=data['patch27']
patches28=data['patch28']
patches29=data['patch29']
patches30=data['patch30']
patches31=data['patch31']
patches32=data['patch32']
patches33=data['patch33']
patches34=data['patch34']
patches35=data['patch35']
patches36=data['patch36']
patches37=data['patch37']
patches38=data['patch38']
patches39=data['patch39']
patches40=data['patch40']
 
#create some stimuli using s1-6 to define size and res1-6 to define angularRes. 
ring6a = visual.RadialStim(mywin, tex='None', angularRes=res6,color=1,size=s6,visibleWedge=[0, 90], ori=0, interpolate=False,autoLog=False)
ring6b = visual.RadialStim(mywin, tex='None', angularRes=res6,color=1,size=s6,visibleWedge=[0, 90], ori=90, interpolate=False,autoLog=False)
ring6c = visual.RadialStim(mywin, tex='None', angularRes=res6,color=1,size=s6,visibleWedge=[0, 90], ori=180, interpolate=False,autoLog=False)
ring6d = visual.RadialStim(mywin, tex='None',angularRes=res6, color=1,size=s6,visibleWedge=[0, 90], ori=270, interpolate=False,autoLog=False)
ring5a = visual.RadialStim(mywin, tex='None', angularRes=res5,color=1,size=s5,visibleWedge=[0, 60], ori=0, interpolate=False,autoLog=False)
ring5b = visual.RadialStim(mywin, tex='None', angularRes=res5,color=1,size=s5,visibleWedge=[0, 60], ori=60, interpolate=False,autoLog=False)
ring5c = visual.RadialStim(mywin, tex='None', angularRes=res5,color=1,size=s5,visibleWedge=[0, 60], ori=120, interpolate=False,autoLog=False)
ring5d = visual.RadialStim(mywin, tex='None',angularRes=res5, color=1,size=s5,visibleWedge=[0, 60], ori=180, interpolate=False,autoLog=False)
ring5e = visual.RadialStim(mywin, tex='None',angularRes=res5, color=1,size=s5,visibleWedge=[0, 60], ori=240, interpolate=False,autoLog=False)
ring5f = visual.RadialStim(mywin, tex='None', angularRes=res5,color=1,size=s5,visibleWedge=[0, 60], ori=300, interpolate=False,autoLog=False)
ring4a = visual.RadialStim(mywin, tex='None', angularRes=res4,color=1,size=s4,visibleWedge=[0, 45], ori=0, interpolate=False,autoLog=False)
ring4b = visual.RadialStim(mywin, tex='None', angularRes=res4,color=1,size=s4,visibleWedge=[0, 45], ori=45, interpolate=False,autoLog=False)
ring4c = visual.RadialStim(mywin, tex='None',angularRes=res4, color=1,size=s4,visibleWedge=[0, 45], ori=90, interpolate=False,autoLog=False)
ring4d = visual.RadialStim(mywin, tex='None', angularRes=res4,color=1,size=s4,visibleWedge=[0, 45], ori=135, interpolate=False,autoLog=False)
ring4e = visual.RadialStim(mywin, tex='None', angularRes=res4,color=1,size=s4,visibleWedge=[0, 45], ori=180, interpolate=False,autoLog=False)
ring4f = visual.RadialStim(mywin, tex='None',angularRes=res4, color=1,size=s4,visibleWedge=[0, 45], ori=225, interpolate=False,autoLog=False)
ring4g = visual.RadialStim(mywin, tex='None',angularRes=res4, color=1,size=s4,visibleWedge=[0, 45], ori=270, interpolate=False,autoLog=False)
ring4h = visual.RadialStim(mywin, tex='None',angularRes=res4, color=1,size=s4,visibleWedge=[0, 45], ori=315, interpolate=False,autoLog=False)
ring3a = visual.RadialStim(mywin, tex='None', angularRes=res3,color=1,size=s3,visibleWedge=[0, 45], ori=0, interpolate=False,autoLog=False)
ring3b = visual.RadialStim(mywin, tex='None', angularRes=res3,color=1,size=s3,visibleWedge=[0, 45], ori=45, interpolate=False,autoLog=False)
ring3c = visual.RadialStim(mywin, tex='None',angularRes=res3, color=1,size=s3,visibleWedge=[0, 45], ori=90, interpolate=False,autoLog=False)
ring3d = visual.RadialStim(mywin, tex='None', angularRes=res3,color=1,size=s3,visibleWedge=[0, 45], ori=135, interpolate=False,autoLog=False)
ring3e = visual.RadialStim(mywin, tex='None', angularRes=res3,color=1,size=s3,visibleWedge=[0, 45], ori=180, interpolate=False,autoLog=False)
ring3f = visual.RadialStim(mywin, tex='None',angularRes=res3, color=1,size=s3,visibleWedge=[0, 45], ori=225, interpolate=False,autoLog=False)
ring3g = visual.RadialStim(mywin, tex='None',angularRes=res3, color=1,size=s3,visibleWedge=[0, 45], ori=270, interpolate=False,autoLog=False)
ring3h = visual.RadialStim(mywin, tex='None',angularRes=res3, color=1,size=s3,visibleWedge=[0, 45], ori=315, interpolate=False,autoLog=False)
ring2a = visual.RadialStim(mywin, tex='None', angularRes=res2,color=1,size=s2,visibleWedge=[0, 45], ori=0, interpolate=False,autoLog=False)
ring2b = visual.RadialStim(mywin, tex='None', angularRes=res2,color=1,size=s2,visibleWedge=[0, 45], ori=45, interpolate=False,autoLog=False)
ring2c = visual.RadialStim(mywin, tex='None',angularRes=res2, color=1,size=s2,visibleWedge=[0, 45], ori=90, interpolate=False,autoLog=False)
ring2d = visual.RadialStim(mywin, tex='None', angularRes=res2,color=1,size=s2,visibleWedge=[0, 45], ori=135, interpolate=False,autoLog=False)
ring2e = visual.RadialStim(mywin, tex='None', angularRes=res2,color=1,size=s2,visibleWedge=[0, 45], ori=180, interpolate=False,autoLog=False)
ring2f = visual.RadialStim(mywin, tex='None',angularRes=res2, color=1,size=s2,visibleWedge=[0, 45], ori=225, interpolate=False,autoLog=False)
ring2g = visual.RadialStim(mywin, tex='None',angularRes=res2, color=1,size=s2,visibleWedge=[0, 45], ori=270, interpolate=False,autoLog=False)
ring2h = visual.RadialStim(mywin, tex='None',angularRes=res2, color=1,size=s2,visibleWedge=[0, 45], ori=315, interpolate=False,autoLog=False)
ring1a = visual.RadialStim(mywin, tex='None', angularRes=res1,color=1,size=s1,visibleWedge=[0, 60], ori=0, interpolate=False,autoLog=False)
ring1b = visual.RadialStim(mywin, tex='None', angularRes=res1,color=1,size=s1,visibleWedge=[0, 60], ori=60, interpolate=False,autoLog=False)
ring1c = visual.RadialStim(mywin, tex='None', angularRes=res1,color=1,size=s1,visibleWedge=[0, 60], ori=120, interpolate=False,autoLog=False)
ring1d = visual.RadialStim(mywin, tex='None',angularRes=res1,color=1,size=s1,visibleWedge=[0, 60], ori=180, interpolate=False,autoLog=False)
ring1e = visual.RadialStim(mywin, tex='None',angularRes=res1,color=1,size=s1,visibleWedge=[0, 60], ori=240, interpolate=False,autoLog=False)
ring1f = visual.RadialStim(mywin, tex='None', angularRes=res1,color=1,size=s1,visibleWedge=[0, 60], ori=300, interpolate=False,autoLog=False)
fixation= visual.Circle(win=mywin,lineWidth=0, radius=0.05, edges=32, pos=[0,0],fillColor=(1.0,-1.0,-1.0), contrast =1.0,autoLog=False)

#this loop using your patches1-40 variables to set the contrast for each patch every frame 
clock = core.Clock()
fliptimes = numpy.zeros(nIntervals)
mywin.recordFrameIntervals = True
frameN= 0
for frameN in range(nIntervals):
    ring6a.setContrast(patches1[frameN])#advance contrast
    ring6b.setContrast(patches2[frameN])
    ring6c.setContrast(patches3[frameN])
    ring6d.setContrast(patches4[frameN])
    ring5a.setContrast(patches5[frameN])
    ring5b.setContrast(patches6[frameN])
    ring5c.setContrast(patches7[frameN])
    ring5d.setContrast(patches8[frameN])
    ring5e.setContrast(patches9[frameN])
    ring5f.setContrast(patches10[frameN])
    ring4a.setContrast(patches11[frameN])
    ring4b.setContrast(patches12[frameN])
    ring4c.setContrast(patches13[frameN])
    ring4d.setContrast(patches14[frameN])
    ring4e.setContrast(patches15[frameN])
    ring4f.setContrast(patches16[frameN])
    ring4g.setContrast(patches17[frameN])
    ring4h.setContrast(patches18[frameN])
    ring3a.setContrast(patches19[frameN])
    ring3b.setContrast(patches20[frameN])
    ring3c.setContrast(patches21[frameN])
    ring3d.setContrast(patches22[frameN])
    ring3e.setContrast(patches23[frameN])
    ring3f.setContrast(patches24[frameN])
    ring3g.setContrast(patches25[frameN])
    ring3h.setContrast(patches26[frameN])
    ring2a.setContrast(patches27[frameN])
    ring2b.setContrast(patches28[frameN])
    ring2c.setContrast(patches29[frameN])
    ring2d.setContrast(patches30[frameN])
    ring2e.setContrast(patches31[frameN])
    ring2f.setContrast(patches32[frameN])
    ring2g.setContrast(patches33[frameN])
    ring2h.setContrast(patches34[frameN])
    ring1a.setContrast(patches35[frameN])
    ring1b.setContrast(patches36[frameN])
    ring1c.setContrast(patches37[frameN])
    ring1d.setContrast(patches38[frameN])
    ring1e.setContrast(patches39[frameN])
    ring1f.setContrast(patches40[frameN])
    ring6a.draw()
    ring6b.draw()
    ring6c.draw()
    ring6d.draw()
    ring5a.draw()
    ring5b.draw()
    ring5c.draw()
    ring5d.draw()
    ring5e.draw()
    ring5f.draw()
    ring4a.draw()
    ring4b.draw()
    ring4c.draw()
    ring4d.draw()
    ring4e.draw()
    ring4f.draw()
    ring4g.draw()
    ring4h.draw()
    ring3a.draw()
    ring3b.draw()
    ring3c.draw()
    ring3d.draw()
    ring3e.draw()
    ring3f.draw()
    ring3g.draw()
    ring3h.draw()
    ring2a.draw()
    ring2b.draw()
    ring2c.draw()
    ring2d.draw()
    ring2e.draw()
    ring2f.draw()
    ring2g.draw()
    ring2h.draw()
    ring1a.draw()
    ring1b.draw()
    ring1c.draw()
    ring1d.draw()
    ring1e.draw()
    ring1f.draw()
    fixation.draw()
    if event.getKeys():
        print 'stopped early'
        break
    mywin.logOnFlip(msg='frame=%i' %frameN, level=logging.EXP)
    fliptimes[frameN] = mywin.flip()
if disable_gc:
    gc.enable()
core.rush(False)

#cleanup
mywin.close()

#the rest of the code plots the frames lost 
#calculate some values
intervalsMS = pylab.array(mywin.frameIntervals)*1000
m=pylab.mean(intervalsMS)
sd=pylab.std(intervalsMS)
# se=sd/pylab.sqrt(len(intervalsMS)) # for CI of the mean
nTotal=len(intervalsMS)
nDropped=sum(intervalsMS>(1.5*m))
ifis= (fliptimes[1:]-fliptimes[:-1])*1000

#plot the frameintervals
pylab.figure(figsize=[12,8],)

pylab.subplot2grid((2, 2),(0, 0),colspan=2)
pylab.plot(intervalsMS, '-')
pylab.ylabel('t (ms)')
pylab.xlabel('frame N')
pylab.title("Dropped/Frames = %i/%i = %.3f%%. Process Priority: %s, GC Disabled: %s" %(nDropped,nTotal, 100*nDropped/float(nTotal),process_priority,str(disable_gc)), fontsize=12)
#
pylab.subplot2grid((2, 2),(1, 0))
pylab.hist(intervalsMS, 50, normed=0, histtype='stepfilled')
pylab.xlabel('t (ms)')
pylab.ylabel('n frames')
pylab.title("mywin.frameIntervals\nMean=%.2fms, s.d.=%.2f, 99%%CI(frame)=%.2f-%.2f" %(m,sd,m-2.58*sd,m+2.58*sd), fontsize=12)

#
pylab.subplot2grid((2, 2),(1, 1))
pylab.hist(ifis, 50, normed=0, histtype='stepfilled')
pylab.xlabel('t (ms)')
pylab.ylabel('n frames')
pylab.title("Inter Flip Intervals\nMean=%.2fms, s.d.=%.2f, range=%.2f-%.2f ms"%(ifis.mean(), ifis.std(),ifis.min(), ifis.max()), fontsize=12)
pylab.tight_layout()
pylab.show()

#Save screenshot. Maybe outcomment these line during production.
win.getMovieFrame()   # Defaults to front buffer, I.e. what's on screen now.
win.saveMovieFrame('screenshot')  # save with a descriptive and unique filename.