export type Row = {
  name: string
  wave: number
  done: number
  total: number
  next: string
  isPrivate: boolean
}

declare module 'claude-code' {
  interface PluginState {
    'sir-control-room': { rows: Shaped<Row[]>; stamp: Shaped<number> }
  }
}
