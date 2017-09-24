export let socket = null

export function setUpSocket(newSocket) {
  if (!socket) {
    console.log('Setting up new socket...')
    console.log(newSocket)
    socket = newSocket

  } else {
    console.log('A socket already exists!')
  }
}