import { mount, config, createLocalVue } from '@vue/test-utils'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import HomePage from '../src/pages/HomePage.vue';

const axios = {
    get: () => Promise.resolve({ data: [{ val: 1 }] }),
    post: () => Promise.resolve({ data: [{ val: 1 }] }),
    put: () => Promise.resolve({ data: [{ val: 1 }] }),
}

test('mount Page', async () => {
    // const mockMethod = vi.mock(axios)
    expect(HomePage).toBeTruthy()

    const wrapper = mount(HomePage, {
        global: {
            mocks: { axios }
        }
    });

    expect(wrapper.isVisible()).toBe(true);
})