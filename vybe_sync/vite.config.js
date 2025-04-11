import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    allowedHosts: [
      'd7d5-2401-4900-61b3-9c34-412e-3b80-b926-274.ngrok-free.app'
    ]
  }
})
