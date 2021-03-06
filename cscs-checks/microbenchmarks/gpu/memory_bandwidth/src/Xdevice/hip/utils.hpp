#ifndef __INCLUDED_HIP_UTILS__
#define __INCLUDED_HIP_UTILS__

#include <iostream>
#include <hip/hip_runtime.h>

static inline void checkError(hipError_t errorCode)
{
#  ifdef DEBUG
#    ifndef HOSTNAME_SIZE
#      define HOSTNAME_SIZE 80
#    endif

   if (errorCode != hipSuccess)
   {
      char nid[HOSTNAME_SIZE];
      gethostname(nid, HOSTNAME_SIZE);
      std::cerr << "[" << nid << "] A call to the HIP API returned an error :" <<
        hipGetErrorString(errorCode) << std::endl;
      exit(1);
   }
#  endif
}


void XMallocHost(void ** data, size_t size)
{
  checkError( hipHostMalloc(data, size) );
}

void XFreeHost(void * data)
{
  checkError( hipHostFree(data) );
}

void XMalloc(void ** data, size_t size)
{
  checkError( hipMalloc(data, size) );
}

void XMemcpyAsync(void * in, void * out, size_t size, hipMemcpyKind dir, hipStream_t stream)
{
  checkError( hipMemcpyAsync(out, in, size, dir, stream) );
}

void XMemset( void * in, int val, size_t size)
{
  checkError( hipMemset(in, val, size) );
}

void XFree(void * data)
{
  checkError( hipFree(data) );
}

void XDeviceSynchronize()
{
  checkError( hipDeviceSynchronize() );
}

void XGetDeviceCount(int &devices)
{
  checkError( hipGetDeviceCount(&devices) );
}

void XSetDevice(int device)
{
  checkError( hipSetDevice(device) );
}

void XStreamCreate(hipStream_t * stream)
{
  checkError( hipStreamCreate(stream) );
}

void XStreamDestroy(hipStream_t stream)
{
  hipStreamDestroy(stream);
}

void XDeviceCanAccessPeer(int * hasAccess, int self, int peer)
{
  checkError( hipDeviceCanAccessPeer(hasAccess, self, peer) );
}

void XDeviceEnablePeerAccess(int peer, unsigned int flags)
{
  checkError( hipDeviceEnablePeerAccess(peer, flags) );
}

void XDeviceDisablePeerAccess(int peer)
{
  checkError( hipDeviceDisablePeerAccess(peer) );
}

void XMemcpyPeerAsync(void * dst, int peerDevId, void * src, int srcDevId, size_t size, hipStream_t stream)
{
  checkError( hipMemcpyPeerAsync(dst, peerDevId, src, srcDevId, size, stream) );
}

int XGetLastError()
{
  hipError_t err = hipGetLastError();
  if (err != hipSuccess)
  {
    printf("hipGetLastError returned an error ID %d (%s)", (int)err, hipGetErrorString(err));
    return 1;
  }
  return 0;
}

class XTimer
{
private:
  hipStream_t stream;
  hipEvent_t startEvent, stopEvent;

public:
  XTimer(hipStream_t st = 0) : stream(st)
  {
    hipEventCreate(&startEvent);
    hipEventCreate(&stopEvent);
  }

  void start()
  {
    hipEventRecord(startEvent, stream);
  }

  float stop()
  {
    hipEventRecord(stopEvent, stream);
    hipEventSynchronize(stopEvent);
    float execTime = 0;
    hipEventElapsedTime(&execTime, startEvent, stopEvent);
    return execTime;
  }

  ~XTimer()
  {
    hipEventDestroy(startEvent);
    hipEventDestroy(stopEvent);
  }

};

#endif
