import HomePage from "../pages/Home"
import AboutPage from "../pages/About"
import GalleryPage from "../pages/Gallery"

export const EVENTS = {
    PUSHSTATE: 'pushstate',
    POPSTATE: 'popstate',
}

export const ROUTES = [
    {
        path: '/',
        Component: HomePage
    },
    {
        path: '/about',
        Component: AboutPage
    },
    {
        path: '/esculturas',
        Component: GalleryPage
    }
]