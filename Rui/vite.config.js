import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		proxy:{
			//Proxy API request to FastAPI
			'/api': {
				target:'http://127.0.0.1:8000', //FastAPI server
				changeOrigin: true,
				rewrite: (path) => path.replace(/^\/api/,''), //Remove '/api' prefix when forwarding
			},
		},
	},
});
