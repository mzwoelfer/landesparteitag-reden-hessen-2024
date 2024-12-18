import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue';
import Speeches from '../views/Speeches.vue';


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView,
        },
        {
            path: '/faq',
            name: 'faq',
            component: () => import('../views/FAQView.vue'),
        },
        {
            path: '/speeches/:speaker',
            name: 'Speeches',
            props: true,
            component: Speeches
        },
    ],
})

export default router
