import { mount } from '@vue/test-utils'
import LoginPage from '../src/pages/LoginPage.vue';

const axios = {
    get: () => Promise.resolve({ data: [{ val: 1 }] }),
    post: () => Promise.resolve({ data: [{ val: 1 }] }),
    put: () => Promise.resolve({ data: [{ val: 1 }] }),
}

test('mount Page', async () => {
    expect(LoginPage).toBeTruthy()

    const wrapper = mount(LoginPage, {
        global: {
            mocks: { axios }
        }
    });

    expect(wrapper.isVisible()).toBe(true);

    await wrapper.get('#login').trigger('click')
})