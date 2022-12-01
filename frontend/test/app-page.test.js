import { mount, shallowMount } from '@vue/test-utils'
import App from '../src/App.vue';

test('mount component', async () => {
    expect(App).toBeTruthy()

    const wrapper = shallowMount(App);

    expect(wrapper.isVisible()).toBe(true);
})