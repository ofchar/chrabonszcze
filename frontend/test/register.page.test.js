import { mount } from '@vue/test-utils'
import RegisterPage from '../src/pages/RegisterPage.vue';

const axios = {
    get: () => Promise.resolve({ data: [{ val: 1 }] }),
    post: () => Promise.resolve({ data: [{ val: 1 }] }),
    put: () => Promise.resolve({ data: [{ val: 1 }] }),
}

test('mount Page', async () => {
    expect(RegisterPage).toBeTruthy()

    const wrapper = mount(RegisterPage, {
        global: {
            mocks: { axios }
        }
    });

    expect(wrapper.isVisible()).toBe(true);

    await wrapper.get('#register').trigger('click')
})