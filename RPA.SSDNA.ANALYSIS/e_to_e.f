        implicit real*8(a-h,o-z)
        character*8 bead*3,residue*4,filename*1000
        real x,y,z,CMX,CMY,CMZ,CMX_prot,CMY_prot,CMZ_prot,d_min
	character*8 comm*8,kb*8
        integer index,idnaend, idnastart,nt_in,endphos
        dimension x(100000),y(100000),z(100000)
        character filename1*1000
        character*30 myfile1, myfile2,line


        idnastart=1340
        idnaend=2000	
        endphos=500	
	
        write(*,*)idnaend

        Call System("ls Traj_*.dat > input.txt")

        open(30, FILE='input.txt', ACCESS='sequential',status='old')

        do ifile=1,11

        read(30,*)filename1

        open(1,file=filename1,status="old")  
        write(myfile1,'(a,a,i3.3,a)')'end_dis','_',ifile,'.txt'
        open(13, file=myfile1, position="append")

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        
        read(1,*)no_chain
        do i=1,no_chain
        read(1,*)nc
        enddo
 
        do i=1,idnaend
        read(1,*)index,bead,residue
        enddo

        read(1,*)ntot
c	write(*,*)ntot


	do mstep=1,10000

        read(1,*)kb
        do ij=1,idnaend
        read(1,'(a24)')line
        if (line(1:8)=='********'.or.line(9:16)=='********')then
        continue
        else
        read(1,"(3f8.3)")x(ij),y(ij),z(ij)
	end if
        enddo
        
        dx=(x(idnastart)-x(endphos))
        dy=(y(idnastart)-y(endphos))
        dz=(z(idnastart)-z(endphos))

        dr=sqrt(dx**2+dy**2+dz**2)
	write(13,'(i12,f10.3)')mstep,dr

        read(1,*)comm
	enddo

        close(13)
        enddo

        close(1)
        close(30)
c###############################################
        stop


        end
