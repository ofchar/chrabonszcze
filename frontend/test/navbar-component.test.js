import { mount } from '@vue/test-utils'
import NavbarComponent from '../src/components/NavbarComponent.vue';

const axios = {
    get: () => Promise.resolve({ data: [{ val: 1 }] }),
    post: () => Promise.resolve({ data: [{ val: 1 }] }),
    put: () => Promise.resolve({ data: [{ val: 1 }] }),
}

test('mount component', async () => {
    expect(NavbarComponent).toBeTruthy()

    const wrapper = mount(NavbarComponent, {
        global: {
            mocks: { axios }
        }
    });

    expect(wrapper.isVisible()).toBe(true);

    await wrapper.setData({ _token: 'token' })

    await wrapper.get('#logout').trigger('click')
})